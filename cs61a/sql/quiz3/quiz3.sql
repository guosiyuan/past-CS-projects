-- CS 61A Fall 2014
-- Name:Siyuan Guo
-- Login:bgy

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore"        union
  select "delano"           , "jackson";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31           union
  select "jackson"        , "long"       , 43;

-- All triples of dogs with the same fur that have increasing heights

select "=== Question 1 ===";
select a.name, b.name, c.name from dogs as a, dogs as b, dogs as c where a.fur=b.fur and b.fur=c.fur and c.height>b.height and b.height>a.height;

-- Expected output:
--   abraham|delano|clinton
--   abraham|jackson|clinton
--   abraham|jackson|delano
--   grover|eisenhower|barack
--   jackson|delano|clinton

-- The sum of the heights of at least 3 dogs with the same fur, ordered by sum

select "=== Question 2 ===";
with 
  more_than_three(fur_type, n, last_dog, sum) as (
    select fur, 1, name, height from dogs union
    select fur_type, n+1, name, height+sum from dogs, more_than_three where name>last_dog and fur_type=fur

    )




select fur_type, sum from more_than_three where n>=3 order by sum;

-- Expected output:
--   long|115
--   short|115
--   long|116
--   long|119
--   long|136
--   long|162

-- The terms of g(n) where g(n) = g(n-1) + 2*g(n-2) + 3*g(n-3) and g(n) = n if n <= 3

select "=== Question 3 ===";
with
  li_st(n, num, num_1, num_2) as (
    select 1, 1, 0, 0  union
    select 2, 2, 1, 0 union
    select 3, 3, 2, 1 union
    select n+1, num+2*num_1+3*num_2, num, num_1 from li_st where n<25 and n!=1 and n!=2








    )
select num from li_st where n<=20;

-- Expected output:
--   1
--   2
--   3
--   10
--   22
--   51
--   125
--   293
--   696
--   1657
--   ...
--   9426875

