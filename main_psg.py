#!/usr/bin/python3
'''
	pip install PySimpleGUI requests
'''
import PySimpleGUI as sg, requests
layout = [
	[sg.B('Test', key='test_serv')],
	[sg.I('', key='itext'), sg.B('Send', key='send_text')],
	[sg.ML('', size=(60, 15), key='log')]
]
window = sg.Window('', layout, return_keyboard_events=True)
addr = '127.0.0.1:5000'

while True:
	event, values = window()
	if event in (None, 'Exit'): break

	if event == 'test_serv':
		responce = requests.post(f'http://{addr}/')
		window['log'](responce.text)

	if event == 'send_text':
		itext = values['itext']
		responce = requests.post(f'http://{addr}/', json={'text': itext})
		window['log'](responce.text)

	if 'F1' in event: window['log'](requests.post(f'http://{addr}/exec', json={'i': values['itext']}).text)
