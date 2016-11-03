
(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cddr x) (cdr (cdr x)))
(define (cadar x) (car (cdr (car x))))

(define (zip pairs)
  
  (define (getlst1 pairs)
    (if (null? pairs)
      nil
    (cons (caar pairs) (getlst1 (cdr pairs)))
    ))
  (define (getlst2 pairs)
    (if (null? pairs)
      nil
    (cons (cadar pairs) (getlst2 (cdr pairs)))
    ))

  (define lst1 (getlst1 pairs))
  (define lst2 (getlst2 pairs))
  (cons lst1 (cons lst2 nil))
  )

    


(define c (cons (cons 1 (cons 2 nil)) nil))


(define a (cons (cons 1 (cons 2 nil)) (cons (cons 2 (cons 3 nil)) (cons (cons 3 (cons 4 nil)) (cons (cons 4 (cons 5 nil)) nil)))))


(define b (cons (cons 2 (cons 3 nil)) (cons (cons 3 (cons 4 nil)) (cons (cons 4 (cons 5 nil)) (cons (cons 5 (cons 6 nil)) nil)))))

