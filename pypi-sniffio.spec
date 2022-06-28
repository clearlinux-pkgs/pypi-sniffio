#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sniffio
Version  : 1.2.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/a6/ae/44ed7978bcb1f6337a3e2bef19c941de750d73243fc9389140d62853b686/sniffio-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/ae/44ed7978bcb1f6337a3e2bef19c941de750d73243fc9389140d62853b686/sniffio-1.2.0.tar.gz
Summary  : Sniff out which async library your code is running under
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-sniffio-license = %{version}-%{release}
Requires: pypi-sniffio-python = %{version}-%{release}
Requires: pypi-sniffio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/badge/chat-join%20now-blue.svg
:target: https://gitter.im/python-trio/general
:alt: Join chatroom

%package license
Summary: license components for the pypi-sniffio package.
Group: Default

%description license
license components for the pypi-sniffio package.


%package python
Summary: python components for the pypi-sniffio package.
Group: Default
Requires: pypi-sniffio-python3 = %{version}-%{release}

%description python
python components for the pypi-sniffio package.


%package python3
Summary: python3 components for the pypi-sniffio package.
Group: Default
Requires: python3-core
Provides: pypi(sniffio)

%description python3
python3 components for the pypi-sniffio package.


%prep
%setup -q -n sniffio-1.2.0
cd %{_builddir}/sniffio-1.2.0
pushd ..
cp -a sniffio-1.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408243
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sniffio
cp %{_builddir}/sniffio-1.2.0/LICENSE.APACHE2 %{buildroot}/usr/share/package-licenses/pypi-sniffio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/sniffio-1.2.0/LICENSE.MIT %{buildroot}/usr/share/package-licenses/pypi-sniffio/f8c5fdc67d412f3435473ee8ce595f06d921ca44
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sniffio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-sniffio/f8c5fdc67d412f3435473ee8ce595f06d921ca44

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
