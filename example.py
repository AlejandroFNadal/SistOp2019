#Funcion para BOTON
	def new_row(self, origen):
		"""
			Inserta nuevo registro en una tabla de acuerdo al origen
			Parametros:
				_origen: C = Nueva credencial
				_origen: R = Nuevo router
		"""
		tabla = self.get_tabla(origen=origen)
		
		rowPosition = 0

		# Si la tabla esta vacia o la primer fila tiene datos incompletos, insertamos nueva fila al inicio
		# Si la primer fila de la tabla tiene datos incompletos la hacemos foco para que los datos se insertena alli.
		if tabla.rowCount() == 0 or self.is_complete_row(origen=origen):

			tabla.insertRow(rowPosition)
			if origen == "C":
				# Campo usuario: generamos una celda vacia
				tabla.setItem(rowPosition, 0, QTableWidgetItem(""))
				
				# Campo contraseña: generamos una celda tipo password
				x = QLineEdit()
				x.setText("")
				x.setEchoMode(QLineEdit.Password)
				tabla.setCellWidget(rowPosition, 1, x)
			elif origen == "R":
				# Campo IP: generamos una celda vacia
				tabla.setItem(rowPosition, 0, QTableWidgetItem(""))

				# Campo Credencial: generamos una celda inicializada con el valor 1.
				tabla.setItem(rowPosition, 1, QTableWidgetItem("1"))

				# Campo Estado: generamos una celda tipo checkbox con valor 1.
				item = QTableWidgetItem()
				item.setCheckState(Qt.Checked)
				self.ventana.table_routers.setItem(rowPosition , 2, QTableWidgetItem(item))
			elif origen == "CM" or origen == "CF":
				tabla.setItem(rowPosition, 0, QTableWidgetItem(""))
		
		tabla.setFocus()
		tabla.setCurrentCell(0,0)

	# Funcion para Boton
	def delete(self, origen):
		tabla = self.get_tabla(origen=origen)

		items_selected = [item.row() for item in tabla.selectedIndexes()]

		for i in reversed(range(tabla.rowCount())):
			if i in items_selected:
				tabla.removeRow(i)
###############################################################3


		for row in range(tabla.rowCount()):
			if self.is_complete_row(origen=origen, row=row):
				# Creamos CREDENCIAL
				if origen == "C":
					username = tabla.item(row, 0).text()
					password = tabla.cellWidget(row, 1).text()
					
					parser.add(username= username, password=password)
				elif origen == "R":
					ip = tabla.item(row, 0).text()
					credencial = tabla.item(row, 1).text() 
					estado = False
					if tabla.item(row, 2).checkState() == Qt.Checked:
						estado = True
					parser.add(host=ip, credencial=credencial, state=estado)
				elif origen == "CF":
					print("Escribiendo: %s" % (tabla.item(row, 0).text()))
					parser.write(tabla.item(row, 0).text()+"\n")