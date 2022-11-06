def password(pwd:str, cpt:int, length:int):
    """Generate a wordlist (password).
        pwd : empty string eg. ''
        cpt : interger. eg. 1
        length : interger for pwd length. eg. 6
    """
    
    alpha = 'a;b;c;d;e;f;g;f;i;j;k;l;m;n;o;p;q;r;s;t;u;v;w;x;y;z'
    alpha_list = alpha.split(';')  

    if cpt <= length:
        for letter in alpha_list:
            mdp = pwd + letter
            print(mdp)
            
            with open('brute_f6.txt', 'a') as f:
                f.write(f'{mdp}\n')
            l = cpt +1
            pw = pwd + letter
            password(pw, l, 6)
            

if __name__=="__main__":
    password('', 1, 6)