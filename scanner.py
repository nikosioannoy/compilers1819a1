"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?
NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις
	
	if c>='0' and c<='2': return 'DIGA'	# 0..9 grouped together
	
	if c=='3': return 'DIGB'
	
	if c>='0' and c<='9': return 'DIGC'
	
	if c>='0' and c<='5': return 'DIGD'
	
	if c=='0' : return 'DIGE'
	
	if c=='K' : return 'DIGF'
	
	if c=='T' : return 'DIGG'
	
	if c=='M' : return 'DIGH'
	
	if c=='P' : return 'DIGI'
	
	if c=='S' : return 'DIGJ'
	
	if c=='G' : return 'DIGK'
	
	return c	# anything else
	


def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
	
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 's0': { 'DIGA':'s1','DIGB':'s2' },
       			's1': { 'DIGC':'s3' },
       			's2': { 'DIGD':'s3' },
       			's3': { 'DIGE':'s4' },
       			's4': { 'DIGC':'s5' },
       			's5': { 'DIGC':'s6' },
       			's6': { 'DIGF':'s7', 'DIGH':'s9', 'DIGK':'s12' },
       			's7': { 'DIGG':'s8' },
       		    's9': { 'DIGI':'s10' },
     		    's10': { 'DIGJ':'s11' },
     		    's12': { 'DIGC':'s13' },
     		    's13': { 'DIGC':'s14' },
     		    's14': { 'DIGF':'s15','DIGH':'s17' },
     		    's15': { 'DIGG':'s16' },
     		    's17': { 'DIGI':'s18' },
     		    's18': { 'DIGJ':'s19' },
     		    
     		    
     		  } 

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = { 's8':'WIND_TOKEN',
       		's11':'WIND_TOKEN',
       		's16':'WIND_TOKEN',
       		's19':'WIND_TOKEN'
       		
     	  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('ERROR_TOKEN',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
	