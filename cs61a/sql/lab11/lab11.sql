-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

select "States adjacent to California:";







select s1,s2 from adjacencies where s1='CA';
-- Finds lengths of possible paths between two states
create table distances as
  with
    distance(start, end, hops) as (
    select s1, s2, 1 from adjacencies union
    select start, s2, hops+1 from adjacencies, distance where s1=end and hops<=14

    )
  select * from distance;

select "Lengths of paths between CA and WI:";
select * from distances where start = "CA" and end = "WI" order by hops;

select "States 3 hops from CA:";

select end from distances where start='CA' and hops=3;
select "Long alphabetical paths:";
with
  paths(s, n, last) as (
    select state, 1, state from states union
    select s || ',' || s2, n+1, s2 from adjacencies, paths where s1=last and s2>last
  )
select s from paths where n > 6 order by -n;
