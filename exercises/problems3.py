####
# PROBLEM 3_A
####

# Count the number of times each word comes up in this text (use dictionary, ignore upper case).
# Make a list with all the words that come up more than 6 times...

text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pellentesque viverra convallis. Donec euismod eu orci quis ultrices. Sed non gravida enim. Phasellus pharetra nibh leo, sit amet lacinia leo egestas vitae. Cras sed neque sit amet eros laoreet feugiat eget at lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam tempus ante vitae lectus rhoncus, consequat mollis velit tempus. Sed nibh orci, tristique in fringilla sed, malesuada vitae nisl. Nunc imperdiet imperdiet rutrum. Pellentesque purus odio, fringilla in imperdiet a, blandit quis odio. In hac habitasse platea dictumst. Etiam faucibus dolor a mattis tincidunt.
Sed sodales at mi sed porta. In hac habitasse platea dictumst. Mauris adipiscing mollis consectetur. Aenean a porttitor lectus. Morbi magna turpis, iaculis sit amet interdum eu, sollicitudin laoreet augue. Ut ultrices rutrum auctor. Proin justo magna, vehicula ac varius nec, malesuada eget augue. Duis malesuada diam et felis sagittis rutrum eu sed sem. Sed ullamcorper, nisi pretium fermentum sollicitudin, eros velit aliquet tellus, hendrerit interdum dui arcu ac purus. Ut molestie gravida semper. Pellentesque condimentum placerat neque, lacinia gravida sapien aliquet mattis. Nam scelerisque ipsum ac vestibulum tincidunt. Pellentesque cursus ullamcorper consectetur.
Duis fringilla mattis arcu, nec tempor quam pretium vel. Phasellus quis lectus pellentesque, laoreet quam tempor, viverra sapien. Ut id mi lacinia, adipiscing magna ut, feugiat ante. Morbi eget rhoncus leo, sit amet hendrerit sapien. Nulla interdum tincidunt neque, vel lobortis elit laoreet vel. Pellentesque lectus magna, dapibus quis vulputate eu, adipiscing non felis. Cras quis vehicula urna. In pretium ultricies hendrerit. Sed blandit neque a orci venenatis ultricies.
Proin vehicula quam eros. Proin eu ultrices dui. Suspendisse imperdiet massa vitae erat malesuada, eget facilisis mauris iaculis. Integer eu magna cursus, ullamcorper diam ut, eleifend enim. Mauris laoreet nunc nunc, vel dapibus nisl interdum adipiscing. Cras accumsan erat libero, scelerisque sodales neque mattis ultrices. Cras nisi mi, gravida et felis sit amet, viverra hendrerit risus. Donec vel elit sollicitudin, placerat eros iaculis, feugiat enim. In ultrices urna at magna suscipit, non porttitor sem blandit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ultrices, felis a luctus pharetra, quam nunc bibendum mi, a commodo magna augue non risus. Vestibulum elementum velit in semper consectetur. Quisque bibendum gravida mauris, et gravida eros ultricies at. Suspendisse id ultrices lorem. Fusce ut blandit quam, ac accumsan mi.
Morbi mi odio, accumsan nec turpis quis, malesuada placerat eros. Cras a accumsan diam, non interdum libero. Mauris et ligula urna. Sed euismod suscipit porta. Aliquam erat volutpat. Proin ultrices pharetra magna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse hendrerit sollicitudin condimentum. Cras arcu ante, aliquam sed sem vitae, ultricies luctus tortor. Ut eu semper ante.
'''