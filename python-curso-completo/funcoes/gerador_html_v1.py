def tag_block(text, klass="success"):
    return f'<div class="{klass}">{text}</div>'


if __name__ == '__main__':
    assert tag_block('add with success') == \
        '<div class="success">add with success</div>'

    assert tag_block('impossible to remove', 'error') == \
        '<div class="error">impossible to remove</div>'

    print(tag_block('block'))    