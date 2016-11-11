# virus_scanner
simple virus scanner that checks all files in a given directory for signatures from a given signature file

# How to run the program

Usage: python virus_scanner.py

Example usage and output

Enter directory: /Users/derekleung/Git/virus_scanner/test_directory 
Enter signature file path: /Users/derekleung/Git/virus_scanner/signature_list 
signatures in signature file:
['disdasig\n', 'dood\n']

/Users/derekleung/Git/virus_scanner/test_directory/sample_virus3 contains the following signatures:  ['disdasig\n', 'dood\n']
/Users/derekleung/Git/virus_scanner/test_directory/inner_directory/sample_virus contains the following signatures:  ['disdasig\n']
/Users/derekleung/Git/virus_scanner/test_directory/inner_directory/sample_virus2 contains the following signatures:  ['disdasig\n', 'dood\n']