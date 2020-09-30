Sum_SubApp=df_antes.groupby('Sub Application Name')
Duracion_Antes=Sum_SubApp['Run Time (Sec.)'].sum()
etiquetas=Sum_SubApp.groups

colores=['blue','red','yellow','orange']

#Se especifican las dimensiones del grafico
fig=plt.figure(figsize=(9,6),dpi=80)

#Se construye el grafico
plt.pie(Duracion_Antes,labels=etiquetas,colors=colores,startangle=90,autopct='%1.1f%%')

plt.axis('equal')
plt.show