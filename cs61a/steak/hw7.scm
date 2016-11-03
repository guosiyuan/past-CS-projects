(define (deep-reverse lst)
  (cond 
    ((null? lst) lst)
    ((list? (car lst)) (append (deep-reverse (cdr lst)) (cons (deep-reverse (car lst) ) nil)))
    (else (append (deep-reverse (cdr lst)) (cons (car lst) nil)))





  ))

(define a '(1 (2 3) (4 (5 6) 7)))