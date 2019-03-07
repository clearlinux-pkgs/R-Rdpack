#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rdpack
Version  : 0.10.1
Release  : 4
URL      : https://cran.r-project.org/src/contrib/Rdpack_0.10-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rdpack_0.10-1.tar.gz
Summary  : Update and Manipulate Rd Documentation Objects
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bibtex
Requires: R-gbRd
BuildRequires : R-bibtex
BuildRequires : R-gbRd
BuildRequires : buildreq-R

%description
including functions reprompt() and ereprompt() for updating 'Rd'
    documentation for functions, methods and classes; 'Rd' macros for
    citations and import of references from 'bibtex' files for use in
    'Rd' files and 'roxygen2' comments; 'Rd' macros for evaluating and
    inserting snippets of 'R' code and the results of its evaluation or
    creating graphics on the fly; and many functions for manipulation of
    references and Rd files.

%prep
%setup -q -c -n Rdpack

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538661515

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1538661515
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rdpack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rdpack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rdpack
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library Rdpack|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rdpack/DESCRIPTION
/usr/lib64/R/library/Rdpack/INDEX
/usr/lib64/R/library/Rdpack/Meta/Rd.rds
/usr/lib64/R/library/Rdpack/Meta/features.rds
/usr/lib64/R/library/Rdpack/Meta/hsearch.rds
/usr/lib64/R/library/Rdpack/Meta/links.rds
/usr/lib64/R/library/Rdpack/Meta/nsInfo.rds
/usr/lib64/R/library/Rdpack/Meta/package.rds
/usr/lib64/R/library/Rdpack/Meta/vignette.rds
/usr/lib64/R/library/Rdpack/NAMESPACE
/usr/lib64/R/library/Rdpack/NEWS.md
/usr/lib64/R/library/Rdpack/R/Rdpack
/usr/lib64/R/library/Rdpack/R/Rdpack.rdb
/usr/lib64/R/library/Rdpack/R/Rdpack.rdx
/usr/lib64/R/library/Rdpack/REFERENCES.bib
/usr/lib64/R/library/Rdpack/RStudio/addins.dcf
/usr/lib64/R/library/Rdpack/auto/REFERENCES.el
/usr/lib64/R/library/Rdpack/doc/Inserting_bibtex_references.R
/usr/lib64/R/library/Rdpack/doc/Inserting_bibtex_references.Rnw
/usr/lib64/R/library/Rdpack/doc/Inserting_bibtex_references.pdf
/usr/lib64/R/library/Rdpack/doc/Inserting_figures_and_evaluated_examples.R
/usr/lib64/R/library/Rdpack/doc/Inserting_figures_and_evaluated_examples.Rnw
/usr/lib64/R/library/Rdpack/doc/Inserting_figures_and_evaluated_examples.pdf
/usr/lib64/R/library/Rdpack/doc/index.html
/usr/lib64/R/library/Rdpack/examples/RdpackTester.pdf
/usr/lib64/R/library/Rdpack/examples/RdpackTester/DESCRIPTION
/usr/lib64/R/library/Rdpack/examples/RdpackTester/NAMESPACE
/usr/lib64/R/library/Rdpack/examples/RdpackTester/R/RdpackTester-internal.R
/usr/lib64/R/library/Rdpack/examples/RdpackTester/inst/REFERENCES.bib
/usr/lib64/R/library/Rdpack/examples/RdpackTester/inst/auto/REFERENCES.el
/usr/lib64/R/library/Rdpack/examples/RdpackTester/man/RdpackTester-package.Rd
/usr/lib64/R/library/Rdpack/examples/journal_with_percents.bib
/usr/lib64/R/library/Rdpack/examples/tz.Rd
/usr/lib64/R/library/Rdpack/examples/url_with_percents.bib
/usr/lib64/R/library/Rdpack/help/AnIndex
/usr/lib64/R/library/Rdpack/help/Rdpack.rdb
/usr/lib64/R/library/Rdpack/help/Rdpack.rdx
/usr/lib64/R/library/Rdpack/help/aliases.rds
/usr/lib64/R/library/Rdpack/help/macros/refmacros.Rd
/usr/lib64/R/library/Rdpack/help/paths.rds
/usr/lib64/R/library/Rdpack/html/00Index.html
/usr/lib64/R/library/Rdpack/html/R.css
