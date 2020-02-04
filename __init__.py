# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ValorizaSoloUrbano
                                 A QGIS plugin
 Cálculo da Valorização de Solo Urbano
                             -------------------
        begin                : 2020-01-15
        copyright            : (C) 2020 by João Norberto Destro / joaodestro@gmail.com
        email                : joaodestro@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ValorizaSoloUrbano class from file ValorizaSoloUrbano.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .ValorSoloUrbano import ValorizaSoloUrbano
    return ValorizaSoloUrbano(iface)
