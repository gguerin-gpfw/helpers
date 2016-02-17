import numpy

def dictWalker(d, name=None, l=0):
	if name is not None:
		print 'Walking into dict %s:'%name
	if l==0:
		print '{'
		l += 1
	for k,v in d.items():
		if isinstance(v, dict):
			print '\t'*l + k + ': {'
			dictWalker(v, l=l+1)
			print '\t'*l + '},'
		else:
			if isinstance(k, str):
				k = "'%s'" % k
			print '\t'*l + "%s: %s," % (k, v)
	if l==1:
		print '}'

if __name__ == '__main__':

	d = {
		'test1':{
			'test11': 2,
			'test12': 'str',
			'blah': {'a': 10, 'b': 100}
		},
		'test2':{
			'test12': numpy.ones((2, 20)),
			'test22': numpy.array(xrange(40))
		}
	}
	dictWalker(d, 'test')
