#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-g.data
Version  : 2.4
Release  : 24
URL      : https://cran.r-project.org/src/contrib/g.data_2.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/g.data_2.4.tar.gz
Summary  : Delayed-Data Packages
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
a ddp are available on demand, but do not take up memory until requested.
  You attach a ddp with g.data.attach(), then read from it and assign to it in
  a manner similar to S-PLUS, except that you must run g.data.save() to
  actually commit to disk.

%prep
%setup -q -c -n g.data
cd %{_builddir}/g.data

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589534002

%install
export SOURCE_DATE_EPOCH=1589534002
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library g.data
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library g.data
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library g.data
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc g.data || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/g.data/DESCRIPTION
/usr/lib64/R/library/g.data/INDEX
/usr/lib64/R/library/g.data/Meta/Rd.rds
/usr/lib64/R/library/g.data/Meta/features.rds
/usr/lib64/R/library/g.data/Meta/hsearch.rds
/usr/lib64/R/library/g.data/Meta/links.rds
/usr/lib64/R/library/g.data/Meta/nsInfo.rds
/usr/lib64/R/library/g.data/Meta/package.rds
/usr/lib64/R/library/g.data/Meta/vignette.rds
/usr/lib64/R/library/g.data/NAMESPACE
/usr/lib64/R/library/g.data/R/g.data
/usr/lib64/R/library/g.data/R/g.data.rdb
/usr/lib64/R/library/g.data/R/g.data.rdx
/usr/lib64/R/library/g.data/doc/g.data.R
/usr/lib64/R/library/g.data/doc/g.data.Rnw
/usr/lib64/R/library/g.data/doc/g.data.pdf
/usr/lib64/R/library/g.data/doc/index.html
/usr/lib64/R/library/g.data/help/AnIndex
/usr/lib64/R/library/g.data/help/aliases.rds
/usr/lib64/R/library/g.data/help/g.data.rdb
/usr/lib64/R/library/g.data/help/g.data.rdx
/usr/lib64/R/library/g.data/help/paths.rds
/usr/lib64/R/library/g.data/html/00Index.html
/usr/lib64/R/library/g.data/html/R.css
