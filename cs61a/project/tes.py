(define (subst x old new)
	(cond
	((null? old) x)
	 ((= x (car old)) (car new))
	 (else (subst x (cdr old) (cdr new)))
		)
	)
