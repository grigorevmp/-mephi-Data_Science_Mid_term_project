--dup_names - все люди, которые появляются в bd более одного раза

select * from "BoardingData";

select distinct dn."Name", count(distinct "PassengerBirthDate")
from "boarding_data2" join dup_names dn on boarding_data2."Name" = dn."Name"
group by dn."Name";

-- список всех двойников по именам с возможными др и паспортами
with tab as (
    select distinct dn."Name" as Name, count(distinct "PassengerBirthDate") as Amount
    from "boarding_data2" join dup_names dn on boarding_data2."Name" = dn."Name"
    group by dn."Name"
)
select bd."PassengerBirthDate", bd."PassengerDocument", t.Name
from tab t join boarding_data2 bd on t.Name = bd."Name"
where Amount > 1
order by t.Name;

with tab as (
    select distinct dn."Name" as Name, count(distinct "PassengerBirthDate") as Amount
    from "boarding_data2" join dup_names dn on boarding_data2."Name" = dn."Name"
    group by dn."Name"
),
tab2 as (
    select bd."PassengerBirthDate", bd."PassengerDocument", t.Name as Name
    from tab t join boarding_data2 bd on t.Name = bd."Name"
    where Amount > 1
    order by t.Name
),
tab3 as (
    select distinct "PassengerBirthDate", count(distinct "PassengerDocument") as AmountDoc, count(distinct Name) as AmountNames
    from tab2
    group by "PassengerBirthDate"
)
select distinct tab3."PassengerBirthDate", Name, count(distinct "PassengerDocument") as AmountDoc
from tab3 join tab2 on tab2."PassengerBirthDate" = tab3."PassengerBirthDate"
where AmountNames != AmountDoc
group by tab3."PassengerBirthDate", Name;


with tab as (
    select distinct dn."Name" as Name, count(distinct "PassengerBirthDate") as Amount
    from "boarding_data2" join dup_names dn on boarding_data2."Name" = dn."Name"
    group by dn."Name"
),
tab2 as (
    select bd."PassengerBirthDate", bd."PassengerDocument", t.Name as Name
    from tab t join boarding_data2 bd on t.Name = bd."Name"
    where Amount > 1
    order by t.Name
),
tab3 as   (select distinct "PassengerBirthDate", count(distinct "PassengerDocument") as AmountDoc, count(distinct Name) as AmountNames
    from tab2
    group by "PassengerBirthDate"
    order by "PassengerBirthDate")
select distinct "PassengerBirthDate", AmountDoc, AmountNames
from tab3
where AmountDoc != AmountNames;

select *
from boarding_data2 where "Name" = 'AMALIIA KUDRIAVTSEVA';


with tab as (
    select distinct "PaxName", count(distinct "BirthDate") as amountBD, count(distinct "TravelDoc") as AmountDoc
    from "Sirena-export-fixed"
    group by "PaxName"
)
select *
from tab where AmountDoc - amountBD = 3 ;

select "PaxName", "BirthDate", "TravelDoc", "DepartDate", "From", "Dest"
from "Sirena-export-fixed" where "PaxName" = 'УЛЬЯНОВА КАРИНА КОНСТАНТИНОВНА'
order by "DepartDate";



with tab as (select "PaxName", count(*) as Amount
from "Sirena-export-fixed"
where "Baggage" = '0PC'
group by "PaxName"
order by Amount desc)
select tab."PaxName" as Name, count(*) as Flight_Amount, Amount as Amount_without_bag
from tab join "Sirena-export-fixed" on tab."PaxName" = "Sirena-export-fixed"."PaxName"
where Amount > 4
group by tab."PaxName", Amount_without_bag
order by Amount_without_bag desc;

select "PaxName", "DepartDate", "From", "Dest", "Baggage"
from "Sirena-export-fixed" where "PaxName" = 'СОКОЛОВА НАТАЛЬЯ АРСЕНЬЕВНА'
order by "DepartDate";

-- без багажа boarding_data
with tab as (
    select "Name", count(*) as Amount
from boarding_data2
where "Baggage" = 'None'
group by "Name"
order by Amount desc)
select count(*)
from tab
where Amount = 1;

select *
from boarding_data2 where "Name" = 'IAROMIR OVSIANNIKOV';

--Бонусные программы
with tabFB as (select distinct "Name", count(distinct "Number") as AmountFB
from unique_bonus where "Programm" = 'FB'
group by "Name"),
     tabFB_full as (select distinct unique_bonus."Name", coalesce(AmountFB, 0) as AmountFB
from unique_bonus left join tabFB on unique_bonus."Name" = tabFB."Name"),
     tabKE as (select distinct "Name", count(distinct "Number") as AmountKE
from unique_bonus where "Programm" = 'KE'
group by "Name"),
     tabKE_full as (select distinct unique_bonus."Name", coalesce(AmountKE, 0) as AmountKE
from unique_bonus left join tabKE on unique_bonus."Name" = tabKE."Name"),
     tabDT as (select distinct "Name", count(distinct "Number") as AmountDT
from unique_bonus where "Programm" = 'DT'
group by "Name"),
     tabDT_full as (select distinct unique_bonus."Name", coalesce(AmountDT, 0) as AmountDT
from unique_bonus left join tabDT on unique_bonus."Name" = tabDT."Name"),
     tabSU as (select distinct "Name", count(distinct "Number") as AmountSU
from unique_bonus where "Programm" = 'SU'
group by "Name"),
     tabSU_full as (select distinct unique_bonus."Name", coalesce(AmountSU, 0) as AmountSU
from unique_bonus left join tabSU on unique_bonus."Name" = tabSU."Name")
select distinct tabFB_full."Name", AmountFB, AmountKE, AmountDT, AmountSU
from tabFB_full
    join tabKE_full on tabKE_full."Name" = tabFB_full."Name"
    join tabDT_full on tabDT_full."Name" = tabFB_full."Name"
    join tabSU_full on tabSU_full."Name" = tabFB_full."Name"
    join pointz on tabFB_full."Name" = pointz."Name"
where AmountFB = 4 or AmountKE = 4 or AmountDT = 4 or AmountSU = 4;


select * from pointz where "Name" = 'MARAT KONOVALOV';
