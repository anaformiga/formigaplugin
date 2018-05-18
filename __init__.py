# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Formiga
                                 A QGIS plugin
 this plugin is to turn insects into ants
                             -------------------
        begin                : 2018-05-18
        copyright            : (C) 2018 by ana formiga
        email                : carolinaformiga95@gmail.com
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
    """Load Formiga class from file Formiga.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .formiga import Formiga
    return Formiga(iface)
