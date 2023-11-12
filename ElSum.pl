sum_list([], 0).
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, Sum1),       
    Sum is Head + Sum1.        

?- sum_list([1, 2, 3, 4, 5, 25], X).
domains