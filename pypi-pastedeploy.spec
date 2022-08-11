#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x27D6E89D63C42919 (mmericke@gmail.com)
#
Name     : pypi-pastedeploy
Version  : 2.1.1
Release  : 67
URL      : https://files.pythonhosted.org/packages/3f/98/179626030d6b3f04e4471aae01f1eae7539347fa7bb8f1228ea4ed600054/PasteDeploy-2.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3f/98/179626030d6b3f04e4471aae01f1eae7539347fa7bb8f1228ea4ed600054/PasteDeploy-2.1.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/3f/98/179626030d6b3f04e4471aae01f1eae7539347fa7bb8f1228ea4ed600054/PasteDeploy-2.1.1.tar.gz.asc
Summary  : Load, configure, and compose WSGI applications and servers
Group    : Development/Tools
License  : MIT
Requires: pypi-pastedeploy-license = %{version}-%{release}
Requires: pypi-pastedeploy-python = %{version}-%{release}
Requires: pypi-pastedeploy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi-nose

%description
URIs. These URIs can refer to Python eggs for INI-style configuration

%package license
Summary: license components for the pypi-pastedeploy package.
Group: Default

%description license
license components for the pypi-pastedeploy package.


%package python
Summary: python components for the pypi-pastedeploy package.
Group: Default
Requires: pypi-pastedeploy-python3 = %{version}-%{release}

%description python
python components for the pypi-pastedeploy package.


%package python3
Summary: python3 components for the pypi-pastedeploy package.
Group: Default
Requires: python3-core
Provides: pypi(pastedeploy)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-pastedeploy package.


%prep
%setup -q -n PasteDeploy-2.1.1
cd %{_builddir}/PasteDeploy-2.1.1
pushd ..
cp -a PasteDeploy-2.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656393092
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pastedeploy
cp %{_builddir}/PasteDeploy-2.1.1/license.txt %{buildroot}/usr/share/package-licenses/pypi-pastedeploy/391729571488896efa70494919f96aab67116ad1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/paste/deploy/paster_templates/paste_deploy/+package+/sampleapp.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/paste/deploy/paster_templates/paste_deploy/+package+/wsgiapp.py_tmpl
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pastedeploy/391729571488896efa70494919f96aab67116ad1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
