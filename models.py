# -*- coding: utf-8 -*-

from odoo import models,fields

class alumno(models.Model):
    _name = 'proyecto.alumno'

    nombre = fields.Char()
    clase= fields.Many2one('proyecto.alumnos', string="Clase")
 
class clase(models.Model):
    _name = 'proyecto.clase'


    nombre = fields.Char()
    alumnos= fields.One2many('proyecto.alumno','clase',string="alumnos")
    equipos= fields.Many2one('proyecto.equipo', string="equipos")
class equipo(models.Model):
    _name = 'proyecto.equipo'

    nombre= fields.Char()
    clase= fields.One2many('proyecto.clase','equipos',string="clase")
    deporte= fields.One2many('proyecto.deporte','equipos',string="deportes")
    color = fields.Selection((('blanco', 'Blanco'), ('negro', 'Negro'), ('azul', 'Azul'), ('rojo', 'Rojo'), ('verde', 'Verde')))

class deporte(models.Model):
    _name = 'proyecto.deporte'

    nombre= fields.Char()
    equipos= fields.Many2one('proyecto.equipo', string="equipos")
    partidos= fields.Many2one('proyecto.partido', string="partidos")

  
class partido(models.Model):
    _name = 'proyecto.partido'

    deporte = fields.One2many('proyecto.deporte','partidos', string="partidos")
    