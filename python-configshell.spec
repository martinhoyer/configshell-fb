# Copyright 2011, Red Hat
# The Fedora package is built from this spec file. Packit copies it to
# Fedora dist-git with every release (propose_downstream in .packit.yaml),
# so change the packaging here rather than in dist-git.

Name:           python-configshell
License:        Apache-2.0
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        2.0.3
Release:        %autorelease
URL:            https://github.com/open-iscsi/configshell-fb
Source:         %{pypi_source configshell}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
A framework to implement simple but nice configuration-oriented\
command-line interfaces.

%description %_description

%package -n python3-configshell
Summary:        A framework to implement simple but nice CLIs
# Published on PyPI as configshell-fb until version 2.0.3. Keep providing
# the old name for packages that still depend on it.
Provides:       python3dist(configshell-fb) = %{version}
Provides:       python%{python3_version}dist(configshell-fb) = %{version}

%description -n python3-configshell %_description

%prep
%autosetup -n configshell-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# configshell_fb is a deprecated alias of configshell
%pyproject_save_files -l configshell configshell_fb

%check
%pyproject_check_import

%files -n python3-configshell -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
