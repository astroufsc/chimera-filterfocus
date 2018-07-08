chimera-filterfocus plugin
===========================

This is a plugin for the chimera observatory control system
https://github.com/astroufsc/chimera.

It subscribes to filter wheel `filterChange()` events to apply offsets in the focuser position for different filter
thickness and refraction indexes.

Usage
-----

Install this plugin and configure names and offsets for each filter in `focus_filters` and `focus_difference` config
parameters. To move steps INm you should use a negative number, to move OUT, a positive one.

Installation
------------

::

    pip install -U https://github.com/astroufsc/chimera-filterchange/archive/master.zip


Configuration Example
---------------------

::
        focuser: /Focuser/0
        filterwheel: /FilterWheel/0
        focus_filters: "U B V R I"  # Filter names in order of focus_difference
        focus_difference: "-100 0 0 0 0",  # e.g. from V to U, move -100 (IN), from U to V, move +100 (OUT)

Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-filterfocus/
