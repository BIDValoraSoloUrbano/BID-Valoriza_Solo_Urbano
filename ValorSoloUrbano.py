# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ValorizaSoloUrbano
                                 A QGIS plugin
 Cálculo da Valorização de Solo Urbano
                              -------------------
        begin                : 2020-01-15
        git sha              : $Format:%H$
        copyright            : (C) 2020 by João Norberto Destro / joaodestro@gmail.com
        email                : joaodestro@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QFileDialog

# Biblioteca de tipo de dados
from PyQt4.QtCore import QVariant
from qgis.core import QgsField, QgsGeometry

# Messagem
from qgis.gui import QgsMessageBar
from qgis.utils import iface

# Initialize Qt resources from file resources.py
import resources

# Import the code for the dialog
from ValorSoloUrbano_dialog import ValorizaSoloUrbanoDialog
import os.path
import math
import locale

class ValorizaSoloUrbano:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgisInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ValorizaSoloUrbano_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&_Valoriza Solo Urbano')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'ValorizaSoloUrbano')
        self.toolbar.setObjectName(u'ValorizaSoloUrbano')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ValorizaSoloUrbano', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dlg = ValorizaSoloUrbanoDialog()

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/ValorizaSoloUrbano/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Obra Linear'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginVectorMenu(
                self.tr(u'&_Valoriza Solo Urbano'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):

        #CARREGA A LISTA DOS NOMES DOS LAYER DA TOC
        layers = self.iface.legendInterface().layers()
        layer_list = []
        i = 0
        iObra = 0
        iLote = 0
        for layer in layers:
            nomeLayer = layer.name()
            layer_list.append(nomeLayer)
            if 'obra' in str(nomeLayer).lower():
                iObra = i
            if 'lote' in str(nomeLayer).lower():
                iLote = i
            i = i + 1

        #SELECIONAR O SHP DA OBRA
        self.dlg.comboBox_obra.clear()
        self.dlg.comboBox_obra.addItems(layer_list)

        #SELECIONAR O SHP DOS LOTES
        self.dlg.comboBox_lote.clear()
        self.dlg.comboBox_lote.addItems(layer_list)

        #SELECIONAR OBRA E LOTE AUTOMATICAMENTE
        self.dlg.comboBox_obra.setCurrentIndex(iObra)
        self.dlg.comboBox_lote.setCurrentIndex(iLote)

        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            # pass

            selectedLayerIndex = self.dlg.comboBox_obra.currentIndex()
            selectedLayerObra = layers[selectedLayerIndex]
            selectedLayerIndex = self.dlg.comboBox_lote.currentIndex()
            selectedLayerLote = layers[selectedLayerIndex]

            #LISTA DOS CAMPOS OBTIDA PELO dataProvider
            lotes = selectedLayerLote.dataProvider()

            #CRIACAO DE NOVO CAMPOS EM LOTES
            field_dista1_index = lotes.fields().indexFromName("area")
            if field_dista1_index == -1:
                #CRIAR O CAMPO AREA, POIS ELE NAO EXISTE
                lotes.addAttributes([QgsField("area", QVariant.Double, 'double', 20, 2)])
                selectedLayerLote.updateFields()

            field_dista1_index = lotes.fields().indexFromName("distobra")
            if field_dista1_index == -1:
                #CRIAR O CAMPO DISTOBRA, POIS ELE NAO EXISTE
                lotes.addAttributes([QgsField("distobra", QVariant.Double, 'double', 20, 2)])
                selectedLayerLote.updateFields()

            field_valor_index = lotes.fields().indexFromName("valor")
            if field_valor_index == -1:
                #CRIAR O CAMPO VALOR, POIS ELE NAO EXISTE
                lotes.addAttributes([QgsField("valor", QVariant.Double, 'double', 20, 2)])
                selectedLayerLote.updateFields()

            field_valtot_index = lotes.fields().indexFromName("valtot")
            if field_valtot_index == -1:
                #CRIAR O CAMPO VALTOT, POIS ELE NAO EXISTE
                lotes.addAttributes([QgsField("valtot", QVariant.Double, 'double', 20, 2)])
                selectedLayerLote.updateFields()

            #DETECTA OS IDs DOS NOVOS CAMPOS CRIADOS
            id_field_area = lotes.fields().indexFromName('area')
            id_field_distObra = lotes.fields().indexFromName('distobra')
            id_field_valor = lotes.fields().indexFromName('valor')
            id_field_valtot = lotes.fields().indexFromName('valtot')

            #PARAMETRO PARA O CALCULO DE VALOR1
            if self.dlg.radioButton_pav.isChecked():
                #radioButton_pavimentacao_via
                localmin1 = 0.00
                localmax1 = 100.00
                valor1 = 10.00
                localmin2 = 100.00
                localmax2 = 200.00
                valor2 = 5.00
                localmin3 = 200.00
                localmax3 = 300.00
                valor3 = 2.50

            #LE AS COORDENADA DA OBRA
            for fObra in selectedLayerObra.getFeatures():
                geomObra = fObra.geometry()

            #INICIO DA EDICAO DOS DADOS
            selectedLayerLote.startEditing()

            #LE AS COORDENADA DOS LOTES
            val_tot_geral=0.00
            val_tot_area=0.00
            tot_lotes=0
            for fLote in selectedLayerLote.getFeatures():
                id = fLote.id()
                geomLote = fLote.geometry()

                #CALCULO DA DISTANCIA ENTRE POLIGONOS E AREA DO LOTE
                distobra = QgsGeometry.distance(geomLote, geomObra)
                val_area = QgsGeometry.area(geomLote)

                valor = 0.0
                if localmin1 <= distobra < localmax1:
                    valor = valor1
                elif localmin2 <= distobra < localmax2:
                    valor = valor2
                elif localmin3 <= distobra < localmax3:
                    valor = valor3

                #TOTALIZA VALOR POR LOTE
                val_tot_lot=val_area * valor

                #TOTALIZA POR LOTE AFETADO
                if valor > 0:
                    val_tot_area = val_tot_area + val_area
                    val_tot_geral = val_tot_geral + val_tot_lot
                    tot_lotes = tot_lotes + 1

                #GRAVA OS VALORES NA CAMADA DE LOTES
                selectedLayerLote.changeAttributeValue(id, id_field_area, geomLote.area())
                selectedLayerLote.changeAttributeValue(id, id_field_distObra, distobra)
                selectedLayerLote.changeAttributeValue(id, id_field_valor, valor)
                selectedLayerLote.changeAttributeValue(id, id_field_valtot, val_tot_lot)

            #COMITA AS MUDANCAS
            selectedLayerLote.commitChanges()

            iface.messageBar().pushMessage("BID - VALORIZA SOLO URBANO", "Calculo realizado com sucesso!",
                                           level=QgsMessageBar.INFO, duration=5)

            #ABRE A TABELA DE ATRIBUTOS DOS LOTES
            iface.showAttributeTable(selectedLayerLote)

            #FORMATA A MENSAGEM
            tot_tributo_geral = val_tot_geral * 0.02
            tot_valor = round(val_tot_geral,2)
            tot_area  = round(val_tot_area,2)
            tot_tributo = round(tot_tributo_geral,2)
            tot_valor_formatado = '{0:,}'.format(tot_valor).replace(',','.')
            tot_tributo_formatado = '{0:,}'.format(tot_tributo).replace(',','.')
            tot_area_formatado  = '{0:,}'.format(tot_area).replace(',','.')
            tot_lotes_formatado = '{0:,}'.format(tot_lotes).replace(',','.')
            txt1 = '%s' % ("VALORIZA SOLO URBANO\n\n\n")
            txt2 = 'Total Lotes......................=  %s\n\n' % (tot_lotes_formatado)
            txt3 = 'Total Area (m2)..............=  %s\n\n' % (tot_area_formatado)
            txt4 = 'Total Incremento ($).....=  %s\n\n' % (tot_valor_formatado)
            txt5 = 'Total Aliquota a 2 ($).....=  %s\n' % (tot_tributo_formatado)
            txt6 = '%s%s%s%s%s' % (txt1, txt2, txt3, txt4, txt5)
            import ctypes
            MessageBox = ctypes.windll.user32.MessageBoxA
            MessageBox(None, txt6, '   B I D  /  A B R A S F', 0)


