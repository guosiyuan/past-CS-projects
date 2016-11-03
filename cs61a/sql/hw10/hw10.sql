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
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------


-- The names of all "toy" and "mini" dogs
create table dog_size as
  with
    dog_size(name, size) as (
      select d.name , s.size 
          from dogs as d, sizes as s 
          where d.height>s.min and 
          d.height<=s.max
    )

  select * from dog_size;
select name from dog_size where size='toy' or size='mini';
-- Expected output:
--   abraham
--   eisenhower
--   fillmore
--   grover
--   herbert

-- All dogs with parents ordered by decreasing height of their parent
select a.child from parents as a, dogs as b where a.parent=b.name order by -b.height;
-- Expected output:
--   herbert
--   fillmore
--   abraham
--   delano
--   grover
--   barack
--   clinton

-- Sentences about siblings that are the same size

with 
  siblings(dog1, dog1size,dog2, dog2size) as (
    select a.child, b.size, c.child, d.size
    from parents as a, dog_size as b, parents as c, dog_size as d
    where a.child<c.child and a.parent=c.parent and a.child=b.name and c.child=d.name

    )


    
select dog1 || ' and ' || dog2 || ' are ' || dog1size || ' siblings'
    from siblings
    where dog1size=dog2size;
-- Expected output:
--   barack and clinton are standard siblings
--   abraham and grover are toy siblings

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height

with
  sum_counter(last_dog,last_height, n, sum_height) as (
    select name,height, 1, height from dogs union
    select last_dog || ',' || name,height, n+1, sum_height+height from dogs, sum_counter where n<4 and height>last_height
    )




select last_dog, sum_height from sum_counter where n=4 and sum_height>170 order by sum_height;
-- Expected output:
--   abraham, delano, clinton, barack|171
--   grover, delano, clinton, barack|173
--   herbert, delano, clinton, barack|176
--   fillmore, delano, clinton, barack|177
--   eisenhower, delano, clinton, barack|180

-- All non-parent relations ordered by height difference
select "REPLACE THIS LINE WITH YOUR SOLUTION";
-- Expected output:
--   fillmore|barack
--   eisenhower|barack
--   fillmore|clinton
--   eisenhower|clinton
--   eisenhower|delano
--   abraham|eisenhower
--   grover|eisenhower
--   herbert|eisenhower
--   herbert|fillmore
--   fillmore|herbert
--   eisenhower|herbert
--   eisenhower|grover
--   eisenhower|abraham
--   delano|eisenhower
--   clinton|eisenhower
--   clinton|fillmore
--   barack|eisenhower
--   barack|fillmore


