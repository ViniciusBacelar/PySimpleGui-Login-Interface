import PySimpleGUI as ps


def window_login():
    ps.theme('Dark')
    """
    It creates a window with a layout that contains a text element, an input element, another text
    element, another input element, a button, another button, and another text element
    :return: A window object
    """
    layout = [[ps.Text('Username'),
               ps.Input(key='Username', size=(20, 1))],
              [
                  ps.Text('Password'),
                  ps.Input(key='Password', password_char='*', size=(20, 1))
              ], [ps.Button('Login'),
                  ps.Button('Register')], [ps.Text('', key='Message')]],

    return ps.Window('Login Window', layout=[layout], finalize=True)


def window_register():
    ps.theme('Dark')
    """
    It creates a window with a text box for username, a text box for password, a text box for confirming
    password, and a button to confirm the registration
    :return: A window object
    """
    layout = [[
        ps.Text('Username'),
        ps.Input(key='Register_username', size=(20, 1))
    ],
              [
                  ps.Text('Password'),
                  ps.Input(key='Register_password',
                           password_char='*',
                           size=(20, 1))
              ],
              [
                  ps.Text('Repeat password'),
                  ps.Input(key='Confirm_register_password',
                           password_char='*',
                           size=(20, 1))
              ], [ps.Button('Confirm Register'),
                  ps.Button('Back')], [ps.Text('', key='Message')]],
    return ps.Window('Register Window', layout=layout, finalize=True)


# Creating two variables, window1 and window2, and assigning them the values returned by the functions
# window_login() and None.
window1, window2 = window_login(), None
register_username, register_password = None, None

# A loop that reads all the windows and assigns the values to the variables window, event, and values.
while True:
    window, event, values = ps.read_all_windows()
    # Checking if the window is closed and if it is, it breaks the loop.
    if window == window1 and event == ps.WIN_CLOSED:
        break
    if window == window2 and event == ps.WIN_CLOSED:
        window2.hide()
        window1.un_hide()
    if window == window1 and event == 'Register':
        window2 = window_register()
        window1.hide()
    if window == window2 and event == 'Back':
        window2.hide()
        window1.un_hide()

    if window == window2 and event == 'Confirm Register':
        register_username = values['Register_username']
        register_password = values['Register_password']
        confirm_register_password = values['Confirm_register_password']
        if ((register_username == '' or None)
                and (register_password == '' or None)
                and (confirm_register_password == '' or None)):
            ps.popup('Invalid username or password')
        elif len(str(register_username)) <= 7:
            ps.popup('Username too short')
        elif len(str(register_username)) >= 8 and (register_password !=
                                                   confirm_register_password):
            ps.popup('Unmatched Password')
        elif len(str(register_username)) >= 8 and len(
                str(register_password)) <= 7:
            ps.popup('Password is too short')
        elif len(str(register_username)) >= 8 and len(
                str(register_password)) >= 8 and len(
                    str(confirm_register_password)):
            ps.popup('Successfully registered')

    if window == window1 and event == 'Login':
        username = values['Username']
        password = values['Password']
        if username == None or password == None or username == '' or password == '':
            ps.popup('Incorrect username or password')
        elif len(str(username)) <= 7 or len(str(password)) <= 7:
            ps.popup('Incorrect username or password')
        if len(str(username)) >= 8 and len(str(password)) >= 8:
            if username == register_username and password == register_password:
                ps.popup('Login successful')
    if window == window2 and event == 'Confirm register':
        register_username = values['Register username']
        register_password = values['Register password']
