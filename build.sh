#!/bin/bash

generate_docs() {
    read -p "Install modules?[y/n]: " cont
    if [ "$cont" = "y" ]
    then
        install_modules
    else if [ "$cont" != "n" ]
    then
        printf "Unkown command, assumming yes"
        install_modules
    {
        cd docs
        printf "generating docs\n"
        command make $1 %%
    } || { # Executed on failure
        printf "Making documentation failed\n"
        printf "Could it be an unsupported form of documentation?\n"
        printf "Please assert that modules have been installed already\n"
        cd ..
        read -p "Install modules?[y/n]: " cont
        if [ "$cont" = "y" ]
        then
            install_modules
        else if [ "$cont" != "n" ]
        then
            printf "Unkown command, assumming yes"
            install_modules

    }
}

install_modules() {
    {
        printf "installing modules\n"
        command pip3 install -r requirements.txt
    } ||  # Executed on failure
        printf Installation of required modules failed.
        printf Make sure pip3 and python3 are installed.
    }
}

print_help() {
    printf "Proper Usage: ./setup [Flags]\n"
    printf "[Flags]:\n"
    printf "\t-g [type]\n"
    printf "\t   -- Generates documentation of type [type], if type is not provided, the program asks for type\n"
    printf "\t-m\n"
    printf "\t   -- Installs pip modules\n"
}


if [ "$1" != "" ]
then
    if [ "$1" = "-g" ] # Generating documentation
    then
        if [ "$2" != "" ] # Target is given
        then
            generate_docs $2
        else # Target is not given
            read -p "What form of documentation do you want to generate: " form
            generate_docs form
        fi
    elif [ "$1" = "-m" ] # Installing modules
    then
        install_modules
    else
        printf "Unkown command\n"
        print_help

    printf "Setup completed\n"
else
    print_help
fi
