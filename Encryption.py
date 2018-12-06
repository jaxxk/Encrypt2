


def rot13(in_char):
	rot13_dict = {
			'a':'n',
			'b':'o',
			'c':'p',
			'd':'q',
			'e':'r',
			'f':'s',
			'g':'t',
			'h':'u',
			'i':'v',
			'j':'w',
			'k':'x',
			'l':'y',
			'm':'z',
			'n':'a',
			'o':'b',
			'p':'c',
			'q':'d',
			'r':'e',
			's':'f',
			't':'g',
			'u':'h',
			'v':'i',
			'w':'j',
			'x':'k',
			'y':'l',
			'z':'m',
			}
	out_char = in_char
	if rot13_dict.has_key(in_char):
		out_char = rot13_dict[in_char]
	return out_char

if __name__== "__main__":
	# define all variables
	user_text = raw_input("Enter some text: ")
	user_list = list(user_text)
	output_list = []
	# start encryption process
	for x in user_list:
		y = rot13(x)
		output_list.append(y)

	rotted = "".join(output_list)
	print rotted