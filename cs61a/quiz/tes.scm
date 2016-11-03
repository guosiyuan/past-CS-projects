

(define (tally names)
  
    (define unique_names (unique names))
    (apply-to-all (lambda (x) (cons x (count x names))) unique_names)
    




    
  )

(define (test-tally)
  (print (list 'testing 'tally))
  (assert-equal '((obama . 1))
                '(tally '(obama)))
  (assert-equal '((taft . 3))
                '(tally '(taft taft taft)))
  (assert-equal '((jerry . 2) (brown . 1))
                '(tally '(jerry jerry brown)))
  (assert-equal '((jane . 5) (jack . 2) (jill . 1))
                '(tally '(jane jack jane jane jack jill jane jane)))
  (assert-equal '((jane . 5) (jack . 2) (jill . 1))
                '(tally '(jane jack jane jane jill jane jane jack)))

  )

(define (apply-to-all fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (apply-to-all fn (cdr s)))))

(define (keep-if fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (keep-if fn (cdr s))))
        (else (keep-if fn (cdr s)))))

; Using this helper procedure is optional. You are allowed to delete it.

(define (inside lst item)
  (cond
    ((null? lst) #f)
    ((eq? (car lst) item) #t)
    ((null? (cdr lst)) #f)
    
    (else (inside (cdr lst) item))
    )
  )

(define (unique s)
  (define (unique-helper lst s)
    (cond 
      ((null? s) (reverse lst))
      ((inside lst (car s)) (unique-helper lst (cdr s)))
      (else (define lst (cons (car s) lst)) (unique-helper lst (cdr s))))


      )
  (unique-helper nil s)
  )

(define (reverse lst)
  (cond
   ((null? lst) nil)
    
   (else (append (reverse (cdr lst)) (list (car lst))))
  )
)










; Using this helper procedure is optional. You are allowed to delete it.
(define (count name s)
  
    
  (cond 
    ((null? s) 0)
    ((eq? name (car s)) (+ 1 (count name (cdr s))))
    (else (count name (cdr s)))

    )

  )




(define (fn x) (cons x 6))
(define lst (cons 'jjj (cons 'jjj (cons 'kkk nil))))
(define unique_names (unique lst))