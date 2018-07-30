init 1:
    image pr normal suit = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_normal.png'))
    image pr smile suit = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_smile.png'))
    image pr serios suit = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_serios.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_serios.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_serios.png'))
    image pr sad suit = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_sad.png'))
    image pr cry suit = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((1050, 1080), (0, 0), 'images/sprites/pr_suit.png', (0, 0), 'images/sprites/pr_cry.png'))