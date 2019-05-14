from xml.dom import minidom
xmldoc = minidom.parse('myxml.xml')
xmldoc.normalize()


node1=xmldoc.getElementsByTagName("item")[0]
print("name="+node1.nodeName)
print("attr="+node1.attributes.item(0).value)
print("value="+node1.childNodes[0].nodeValue)
print('*'*20)

itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print('*'*20)

print(itemlist[0].attributes['name'].value)
print('*'*20)

for node in itemlist:
  print(node.childNodes[0].nodeValue)
print('*'*20)

for s in itemlist:
    print(s.attributes['name'].value)
print('*'*20)


#http://streletzcoder.ru/razbiraem-xml-standartnyimi-sredstvami-python/
#Получить значение тега несколько сложнее. 
#Для этого необходимо вначале обратиться к первому дочернему узлу через коллекцию childNodes 
#(с точки зрения стандартного парсера Python значение тега это почему-то дочерний узел) 
#и только после этого получить само значение через свойство nodeValue.
