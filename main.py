def generate_html(input_str):
  # On split l'input en liste de lignes
  lines = input_str.split('\n')

  # On initialise notre string de HTML
  html_str = '<!DOCTYPE html>\n<html>\n<head>\n<title>Ma page</title>\n</head>\n<body>\n'

  # On initialise notre pile de divs
  div_stack = []

  # Pour chaque ligne de l'input
  for line in lines:
    # On compte le nombre de chevrons en début de ligne
    num_chevrons = 0
    while line[num_chevrons] == '>':
      num_chevrons += 1

    # On enlève les chevrons et les espaces en début de ligne
    line_content = line[num_chevrons:].strip()

    # Si la ligne est vide, on ne fait rien
    if not line_content:
      continue

    # On génère la div correspondante
    div_str = f'<div class="{line_content}">'

    # On retire de la pile les divs qui doivent être fermées
    while len(div_stack) > num_chevrons:
      html_str += '</div>\n'
      div_stack.pop()

    # On ajoute la nouvelle div à la pile et au HTML
    html_str += div_str + '\n'
    div_stack.append(line_content)

  # On ferme toutes les divs restantes dans la pile
  while div_stack:
    html_str += '</div>\n'
    div_stack.pop()

  # On ajoute le footer du HTML
  html_str += '</body>\n</html>'

  return html_str


input_str = ""
#">main\n>>main_navbar\n>>>navbar_find\n>>>navbar_subscribe\n>>>navbar_apropos\n>>>navbar_faq\n>>>navbar_aide\n>>main_container1\n>>>container1_slogan1\n>>>container1_subscribe\n>>main_container2\n>>>container2_info\n>>>container2_slogan2\n>>main_container3\n>>>container3_raison1\n>>>container3_raison2\n>>>container3_raison3\n>>>container3_subscribe\n>>main_footer\n>>>footer_find\n>>>footer_subscribe\n>>>footer_confidentialite\n>>>footer_condition\n>>>footer_copyright"
#">search\n>>search_input\n>>search_button"
#">main\n>>main_container1\n>>>container1_form\n>>>>form_courriel\n>>>>>courriel_label\n>>>>>courriel_input\n>>>>form_motdepasse\n>>>>>motdepasse_label\n>>>>>motdepasse_input\n>>>>form_register\n>>>>login\n>>main_container2\n>>>container2_raison1\n>>>container2_raison2\n>>>container2_raison3"

#">hello_bar\n>>bar_text\n>navbar_beauty\n>>logo\n>>search_bar\n>>>bar_container\n>>>>bar_input\n>>>>bar_submit\n>>circulaire\n>>>circulaire_icone\n>>moncompte\n>>>moncompte_text\n>>panier\n>>>panier_icone\n>navbar\n>>navbar_childs\n>>>navbar_child\n>>>>navbar_child_text\n>page\n>>page_main\n>>>main_categories\n>>>>main_category\n>>>>>main_category_text"
html_str = generate_html(input_str)
print(html_str)
f = open("demofile2.txt", "w")
f.write(html_str)
f.close()
