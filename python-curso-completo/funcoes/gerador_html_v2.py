def tag_block(text, klass="success", inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{klass}">{text}</{tag}>'


if __name__ == '__main__':
    print(tag_block('block'))
    print(tag_block('inline e class', 'info', True))
    print(tag_block('info', inline=True))
    print(tag_block(inline=True, text='info', ))
    print(tag_block('falhou', klass='error'))