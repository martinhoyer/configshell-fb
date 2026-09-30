configshell
===========

A Python library for building configuration shells
--------------------------------------------------
configshell is a Python library that provides a framework
for building simple but nice CLI-based applications.

configshell development
-----------------------
configshell is licensed under the Apache 2.0 license. Contributions are welcome.

 * Source repo: [GitHub](https://github.com/open-iscsi/configshell-fb)
 * Bugs: [GitHub](https://github.com/open-iscsi/configshell-fb/issues)
 * Releases: [PyPI](https://pypi.org/project/configshell/)

Packages
--------
configshell is packaged for a number of Linux distributions
including RHEL,
[Fedora](https://src.fedoraproject.org/rpms/python-configshell),
openSUSE, Arch Linux,
[Gentoo](https://packages.gentoo.org/packages/dev-python/configshell-fb), and
[Debian](https://tracker.debian.org/pkg/python-configshell-fb).

Formerly configshell-fb
-----------------------
This project was previously published as `configshell-fb` ("free branch"), a
fork of the original "configshell" code written by RisingTide Systems. The fork
has long been the only maintained version, so the `-fb` suffix has been dropped
and releases are now published on PyPI as `configshell`.

The `configshell_fb` module is kept as a deprecated alias of `configshell`, so
existing `import configshell_fb` code keeps working. New code should
`import configshell`.

If you are upgrading an existing pip installation, uninstall the old
distribution first, since both install the same files:

    pip uninstall configshell-fb
    pip install configshell
