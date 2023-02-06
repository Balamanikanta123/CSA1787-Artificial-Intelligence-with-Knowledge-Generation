% Define the rules
rules([
  rule(a, [b, c]),
  rule(b, [d, e]),
  rule(c, [f]),
  rule(f, [])
]).

% Define the forward chaining algorithm
forward_chain(Goals) :-
  rules(Rules),
  forward_chain(Goals, Rules).

forward_chain([], _).
forward_chain([Goal|Goals], Rules) :-
  (
    infer_goal(Goal, Rules)
  ;
    already_known(Goal)
  ),
  forward_chain(Goals, Rules).

% Infer a goal if possible
infer_goal(Goal, Rules) :-
  member(rule(Goal, Prerequisites), Rules),
  forward_chain(Prerequisites, Rules).

% Check if a goal is already known
already_known(Goal) :-
  fact(Goal).

% Define some facts
fact(d).
fact(e).
