node_file = 'nodes.csv'
edge_file = 'links.csv'
vna_file = 'output.vna'

with open(vna_file, 'w') as outfile:
  with open(node_file) as infile:
    for i, line in enumerate(infile.readlines()):
      if i == 0:
        outfile.write('*Node data\n')
        new_line = ','.join(line.split(",")[1:])
        outfile.write(new_line)
      else:
        new_line = ' '.join(line.split(",")[1:])
        outfile.write(new_line)
  with open(edge_file) as infile:
    for i, line in enumerate(infile.readlines()):
      if i == 0:
        outfile.write('*Tie data\n')
        outfile.write('FROM TO "distance"')
      else:
        items = line.split(",")[1:]
        items[-1] = items[-1].replace('"', '')
        if items[-1][0].isdigit():
          items[-1] = items[-1][0]
          if i > 1:
            new_line = '\n' + ' '.join(items)
          else:
            new_line = ' '.join(items)
          outfile.write(new_line)
    
    
    

