#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sniffio
Version  : 1.2.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/a6/ae/44ed7978bcb1f6337a3e2bef19c941de750d73243fc9389140d62853b686/sniffio-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/ae/44ed7978bcb1f6337a3e2bef19c941de750d73243fc9389140d62853b686/sniffio-1.2.0.tar.gz
Summary  : Sniff out which async library your code is running under
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: sniffio-license = %{version}-%{release}
Requires: sniffio-python = %{version}-%{release}
Requires: sniffio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/badge/chat-join%20now-blue.svg
:target: https://gitter.im/python-trio/general
:alt: Join chatroom

%package license
Summary: license components for the sniffio package.
Group: Default

%description license
license components for the sniffio package.


%package python
Summary: python components for the sniffio package.
Group: Default
Requires: sniffio-python3 = %{version}-%{release}

%description python
python components for the sniffio package.


%package python3
Summary: python3 components for the sniffio package.
Group: Default
Requires: python3-core
Provides: pypi(sniffio)

%description python3
python3 components for the sniffio package.


%prep
%setup -q -n sniffio-1.2.0
cd %{_builddir}/sniffio-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603922867
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sniffio
cp %{_builddir}/sniffio-1.2.0/LICENSE.APACHE2 %{buildroot}/usr/share/package-licenses/sniffio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/sniffio-1.2.0/LICENSE.MIT %{buildroot}/usr/share/package-licenses/sniffio/f8c5fdc67d412f3435473ee8ce595f06d921ca44
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sniffio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/sniffio/f8c5fdc67d412f3435473ee8ce595f06d921ca44

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
