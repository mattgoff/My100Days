from collections import Counter

test_text = """ 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eu elit nec ex congue mollis non nec nunc. Nunc dignissim congue sodales. Integer eget ultrices purus. Ut nisl ipsum, vehicula vel viverra nec, tempor at libero. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent ut pellentesque est, ut euismod tellus. Ut facilisis ex a tellus ullamcorper semper. Aliquam egestas finibus urna eget mattis. Etiam ante elit, consectetur id nisi vitae, suscipit luctus tortor. Quisque vitae aliquet mi, a tincidunt neque.

Sed pellentesque consequat elit nec suscipit. Pellentesque lorem dui, dignissim id ullamcorper vel, suscipit et sapien. Cras porttitor eros eget enim fermentum, at ornare lorem rutrum. Quisque ullamcorper erat nec gravida facilisis. Duis diam ligula, consequat eu enim sed, cursus tristique dui. Vivamus consequat tellus in augue ullamcorper convallis. Nam vel lectus sollicitudin urna blandit feugiat. Etiam sollicitudin arcu ac risus blandit, sit amet commodo nisl semper. Nunc eu eros id leo dapibus sagittis. Duis hendrerit sagittis orci, at feugiat felis.

Cras pretium, velit et elementum condimentum, nulla elit euismod dui, a convallis risus ipsum sed nibh. Donec a nulla in tortor pharetra malesuada id eu erat. In at porta dui, hendrerit facilisis lacus. Nunc commodo mauris ipsum, ut vulputate ex aliquet nec. Sed at ipsum lacus. Curabitur iaculis diam sed enim euismod, at maximus quam cursus. Aenean condimentum libero ipsum, ut egestas lectus venenatis eu. Morbi sagittis quam sit amet nisi maximus, quis egestas tortor ornare. Maecenas ac pellentesque metus. Aenean efficitur aliquam blandit. Aliquam et tortor iaculis, fringilla velit sed, convallis justo. Integer pulvinar, mauris a pharetra cursus, sapien lorem venenatis nisi, sed lobortis mauris tortor quis leo. Donec facilisis aliquam consectetur.

Pellentesque feugiat ex eget metus congue faucibus. Donec elementum, quam pellentesque pretium interdum, ipsum lectus tempor nibh, at sollicitudin sem nulla quis eros. Maecenas eleifend nunc sed mi lobortis auctor. Quisque accumsan, sem et ultrices congue, urna tellus consequat erat, sed eleifend neque mauris in leo. Quisque fermentum purus risus, non commodo elit tincidunt nec. Proin tincidunt dapibus sagittis. Mauris sollicitudin eget lacus vel mollis. Nulla suscipit porttitor dolor a tincidunt. Nam aliquam et eros sit amet lacinia.

Pellentesque commodo, lacus sed auctor eleifend, diam tortor sodales elit, ac dictum nibh magna ac nunc. Nullam efficitur a mauris ut mollis. In tincidunt purus bibendum leo suscipit, congue viverra risus dictum. Phasellus sed neque quis tortor fermentum malesuada. Phasellus ut ultrices ante. Cras vitae vulputate purus. Fusce non molestie quam. Maecenas feugiat tortor vitae risus euismod, vel ultrices leo sodales.
"""

words = test_text.split(" ")

print(Counter(words).most_common(5))