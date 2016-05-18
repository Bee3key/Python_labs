# splitter.py
def split(line, types=None, delimiter=None):
	"""à¡ÈÂ¡ ª§¬¨º §¬ª¨  ¹ ¥¬Â¾¬«©¬§
	½¹¬£¥¦ ¹¬Â¡È¬¡¥ ¹¬.
	¡¹©:
	ÒÒ
	>>> split('GOOG 100 490.50')
	['GOOG', '100', '490.50']
	>>> split('GOOG 100 490.50',[str, int, float])
	['GOOG', 100, 490.5]
	>>>
	ÒÒ
	¬ ¨©¬£¢¡¥º ¡ÈÂ¥ ¹¬È¬«§¦ ¹¬ ¹¬Â£¤¥½© §©¬£¡©,
	¥¬ ©§¦ ¬È©¬Ç¥¬§¤ ¨ª¡È¡¤ «¨»¬¿ §©¬£-¡È«££¤,  «
	©¥¬¡¥¥¬»¬ ¡»¨©¥¡:
	ÒÒ
	>>> split('GOOG,100,490.50',delimiter=',')
	['GOOG', '100', '490.50']
	>>>
	"""
	fields = line.split(delimiter)
	if types:
		fields = [ ty(val) for ty,val in zip(types,fields) ]
	return fields

def half(x):
	"""¬È¡Ë¡ ¹¬£¬¥¨ x. ¡¹©:
	ÒÒ
	>>> half(6.8)
	3.4
	>>>
	"""
	return x/2