// Iterative solution
func reverseString(s string) string {
    reversed := ""

    for i, _ := range s {
        reversed += string(s[(len(s) -1) - i])
    }
    
    return reversed
}


// Recursive solution
func reverseString(s string) string {

	if s == "" {
		return s
	}

	return string(s[len(s) - 1]) + reverseString(s[:len(s) - 1])
}