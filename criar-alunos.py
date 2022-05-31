nome_banco = "classe"
con = sqlite3.connect(nome_banco) 
cur = con.cursor()

Classe=[
 
     (None,João,branco, 17,True,True,masculino,,4,0 )
     (None,Dorival,pardo,18,True,True,masculino,,6,1 ),
     (None,Edmundo,preto,13,True,True,masculino,,3,0 ),
     (None,Carlos,branco, 15,False,True,masculino,5,0),
     (None,Eunice,amarelo,16,False,True,feminino,3,1),
     (None,Ana,preto,15,True,True,feminino,5,0),
     (None,Manuel,branco,13,False,False,masculino,3,0 ),
     (None,Ramiro, amarelo,14,True,True,masculino,5,0 ),
     (None,Joaquim,indigena,13,True,True,masculino,6,0 ) ,
     (None,Floriano,pardo,16,True, True,masculino,3.0),
     (None,Janaína,pardo,17,True,True,feminino,3,0 ),
     (None,César,branco,15,True,True,masculino,5,0 ),
     (None,Américo,pardo,17,False,False,masculino,5,2 ),
     (None,Eunice,preto,12,False,False,feminino,4,0 ),
     (None,Maria,pardo,16,True,False,feminino,5,0 ),
     (None,Roberto,indigena,14,False,True,masculino,6,0),
     (None,Rogério,preto,.15 ,True, True,masculino,4,0),
     (None,Iago,preto,13,True,True ,masculino,6 ,0),       
     (None,Carlos ,  branco,13,False,False,masculino,3,0),
     (None,Gustavo ,pardo,12,True,True,masculino,5,0 ),
     (None,Heitor,preto,12,True,True,masculino,3,0),           
     (None,Márcia,preto,18,True,True,feminino,4,1),           
     (None,Manuela,branco,13,True,True,feminino,4,0),
     (None,Clara,branco,15,False,True,feminino,5,0),
     (None,Ana Luiza,amarelo,16,True,True,feminino,3,0),
     (None, Helena,branco,12,False,False,feminino,5,0),
     (None,Cristina, pardo,14,True,True,feminino,4,0),
     (None,Roselaine,preto,15 ,False,True,feminino,5,0)

    
] 

cur.executemany("INSERT INTO alunos VALUES (?,?,?,?,?,?,?,?)",alunos)

con.commit()