def parseo(file_path):
    Datos = {}
    
    with open(file_path, 'r') as fasta_file:
        registro_id = None
        secuencia = []
        
        for line in fasta_file:
            if line.startswith('>'):
                if registro_id is not None:
                    Datos[registro_id] = ''.join(secuencia)
                registro_id = line.strip()[1:]  # Elimina el '>' y espacios adicionales
                secuencia.clear()
            else:
                secuencia.append(line.strip())
        
        if registro_id is not None:
            Datos[registro_id] = ''.join(secuencia)
    
    return Datos