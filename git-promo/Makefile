# Variables kept in a config file.
include config.mk

# Process training course feedback to identify those who don't use
# version control.
.PHONY : git
git : $(GIT_EMAIL)

$(GIT_EMAIL) : $(RESPONSES) $(GIT_SOURCE)
	$(GIT_EXE) $< ../data/feedback_archive.tsv $(GIT_EMAIL) ../data/emailgitpromo_archive.csv

.PHONY : test-git
test-git :
	$(TEST_GIT_EXE)

.PHONY : clean
clean :
	rm -f $(GIT_EMAIL)
