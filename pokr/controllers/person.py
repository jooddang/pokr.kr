# -*- coding: utf-8 -*-

from collections import Counter, defaultdict, OrderedDict

from flask import current_app

from popong_models.bill import Bill
from popong_models.candidacy import Candidacy
from popong_models.cosponsorship import cosponsorship
from popong_models.person import Person
from popong_models.pledge import Pledge

from .base import Controller


class PersonController(Controller):
    model = 'person'

    @classmethod
    def allies(cls, person, assembly_id=None, threshold=0.5):
        bills = cls.bills_of(person, assembly_id)
        sponsored_bills = (bill for bill in bills if person.id in (p.id for p in bill.representative_people))
        counter = Counter()
        num_sponsored_bills = 0
        for bill in bills:
            followers = current_app.db.session.query(Person.id)\
                              .join(cosponsorship)\
                              .filter(cosponsorship.c.bill_id == bill.id)
            counter = counter + Counter(follower.id for follower in followers if follower.id != person.id)
            num_sponsored_bills += 1

        return OrderedDict(
            (key, (value + .0) / num_sponsored_bills)
                for key, value in counter.most_common(10)\
                if (value + .0) / num_sponsored_bills > threshold
        )

    @classmethod
    def bills_of(cls, person, assembly_id=None):
        query = Bill.query.join(cosponsorship,
                                Bill.id == cosponsorship.c.bill_id)\
                          .join(Person,
                                Person.id == cosponsorship.c.person_id)\
                          .filter_by(id=person.id)\
                          .order_by(Bill.proposed_date.desc())
        if assembly_id:
            query = query.filter(Bill.assembly_id == assembly_id)

        return query

    @classmethod
    def keyword_counts(cls, person, limit=10):
        # TODO: batch calculation or non-blocking operation
        elected_assembly_ids = [candidacy.assembly_id for candidacy in person.candidacies if candidacy.is_elected]

        if not elected_assembly_ids:
            return {}

        latest_assembly_id = max(elected_assembly_ids)
        keywords = (keyword.name
                        for bill in cls.bills_of(person, latest_assembly_id)
                        for keyword in bill.keywords)
        counter = Counter(keywords)

        return dict(counter.most_common(limit))

    @classmethod
    def party_history(cls, person):
        parties_and_assembly_ids = person.parties.add_columns(Candidacy.assembly_id)
        result = []
        prev_party_id = None
        for party, assembly_id in parties_and_assembly_ids:
            if prev_party_id == party.id:
                result[-1][0].append(assembly_id)
            else:
                result.append(([assembly_id], party))
                prev_party_id = party.id
        return [(party, min(assembly_ids), max(assembly_ids)) for assembly_ids, party in result]

    @classmethod
    def pledges_grouped_by_assembly_id(cls, person):
        query = Pledge.query.join(Candidacy,
                                  Candidacy.id == Pledge.candidacy_id)\
                            .join(Person,
                                  Person.id == Candidacy.person_id)\
                            .filter(Person.id == person.id)\
                            .order_by(Pledge.id)

        result = defaultdict(list)
        for pledge in query:
            result[pledge.candidacy.assembly_id].append(pledge)

        return result

