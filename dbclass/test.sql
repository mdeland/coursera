create trigger R5
after update on Highschooler
for each row
when New.grade > 12
begin
  delete from Highschooler where ID = New.ID;
end;
|
create trigger R5b
after update on Highschooler
for each row
when New.grade = Old.grade + 1
begin
  update Highschooler set grade = grade + 1
where ID = (select ID1 from Friend where ID2 = New.ID);
update Highschooler set grade = grade + 1
where ID = (select ID2 from Friend where ID1 = New.ID);
end;

select * from Highschooler order by name, grade;
update Highschooler set grade = grade + 1 where name = 'Austin';
select * from Highschooler order by name, grade;