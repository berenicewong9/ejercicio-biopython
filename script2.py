def  resume_contents ( nombre de archivo ):
	listaOs  =  os . camino . split ( nombre de archivo )
	listaExt  =  os . camino . splitext ( nombre de archivo )
	si ( listaExt [ 1 ] ==  ".gbk" ):
		type_file =  "genbank"
	otra cosa :
		type_file =  "fasta"
	registro  =  lista ( SeqIO . parse ( nombre de archivo , tipo_archivo ))
	#se crea el dic
	diccionario  = {}
	diccionario [ 'Archivo:' ] =  listaOs [ 1 ]
	diccionario [ 'Ruta:' ] =  listaOs [ 0 ]
	diccionario [ 'Num_records:' ] =  len ( registro )
	#dic con listas
	diccionario [ 'Nombres:' ] = []
	diccionario [ 'IDs:' ] = []
	diccionario [ 'Descripciones' ] = []
	#registros
	para  seq_rcd  en  SeqIO . analizar ( nombre de archivo , type_file ):
		d [ 'Nombres:' ]. append ( seq_rcd . Nombre )
		d [ 'ID:' ]. añadir ( seq_rcd . id )
		d [ 'Descripciones' ]. añadir ( descripción de seq_rcd . )
	volver  d

si  _name_  ==  "_main_" :
	resultados  =  resume_contents ( nombre de archivo )
	imprimir ( resultados )
