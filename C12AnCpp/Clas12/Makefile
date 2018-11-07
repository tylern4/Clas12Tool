
INCDIR := inc
SRCDIR := src
OBJDIR := build

INCCORE := $(CORE)/inc
LIBCORE := $(CORE)

INCHIPO := $(HIPO)
LIBHIPO := $(CLAS12TOOL)/lib

SOURCES := $(wildcard $(SRCDIR)/*.cpp)
OBJECTS := $(SOURCES:$(SRCDIR)/%.cpp=$(OBJDIR)/%.o)

CFLAGS  := -Wall -O2 -fPIC -std=c++14
INCLUDES := -I$(INCCORE) -I$(INCHIPO)
LIBS := -L$(LIBCORE) -L$(LIBHIPO)

BUILD := $(shell mkdir -p build)

.PHONY: all clean
all: $(BUILD) $(OBJECTS)
	$(CXX) -I$(INCDIR)  $(INCLUDES) $(LIBS) -o libClas12.so -shared $(CFLAGS)  $(OBJECTS)	

$(OBJECTS): $(OBJDIR)/%.o : $(SRCDIR)/%.cpp
	$(CXX) $(CFLAGS) -I$(INCDIR) $(INCLUDES) $(LIBS) -c $< -o $@

clean:
	rm build/*; rm libClas12.so