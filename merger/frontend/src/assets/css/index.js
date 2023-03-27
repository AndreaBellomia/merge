export const styles = {

    heading1: "text-3xl sm:text-4xl font-semibold",
    heading2: "text-xl sm:text-2xl font-semibold",
    heading3: "text-l sm:text-xl",
    heading4: "text-base sm:text-xl font-extralight",

    flexCenter: "flex justify-center items-center",
    flexStart: "flex justify-start items-start",
    flexEnd: "flex justify-end items-end",

    paddingX: "sm:px-16 px-6",
    paddingY: "sm:py-16 py-6",
    padding: "sm:px-16 px-6 sm:py-16 py-6",

    paddingButton: "py-2 px-4",

    marginX: "sm:mx-16 mx-6",
    marginY: "sm:my-16 my-6",
    margin: "sm:mx-16 mx-6 sm:my-16 my-6",

    floatingActionButtonPositionRight: "fixed bottom-28 right-0",
    floatingActionButtonPositionLeft: "fixed bottom-28 left-0",

    spaceBetweenX: "space-x-4",
    spaceBetweenY: "space-y-4",
};

export const layout = {
    section: `flex md:flex-row flex-col ${styles.paddingY}`,
    sectionReverse: `flex md:flex-row flex-col-reverse ${styles.paddingY}`,

    sectionImgReverse: `flex-1 flex ${styles.flexCenter} md:mr-10 mr-0 md:mt-0 mt-10 relative`,
    sectionImg: `flex-1 flex ${styles.flexCenter} md:ml-10 ml-0 md:mt-0 mt-10 relative`,

    sectionInfo: `flex-1 ${styles.flexStart} flex-col`,
};