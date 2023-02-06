% Define the rules
rules([
  rule(a, [b, c]),
  rule(b, [d, e]),
  rule(c, [f]),
  rule(f, [])
]).

% Define the backward chaining algorithm
backward_chain(Goal) :-
  rules(Rules),
  backward_chain(Goal, Rules).

backward_chain(Goal, Rules) :-
  already_known(Goal), !.

backward_chain(Goal, Rules) :-
  member(rule(Goal, Prerequisites), Rules),
  backward_chain_all(Prerequisites, Rules).

backward_chain_all([], _).
backward_chain_all([Goal|Goals], Rules) :-
  backward_chain(Goal, Rules),
  backward_chain_all(Goals, Rules).

% Check if a goal is already known
already_known(Goal) :-
  fact(Goal).

% Define some facts
fact(d).
fact(e).
