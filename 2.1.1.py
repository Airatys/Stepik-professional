def hide_card(card_number):
    text = card_number.replace(' ', '')
    return ''.join(['*' if i < 12 else j for i, j in enumerate(text)])