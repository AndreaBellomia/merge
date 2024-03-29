export const styles = {

    heading1: "text-3xl sm:text-4xl font-bold",
    heading2: "text-xl sm:text-2xl font-semibold",
    heading3: "text-l sm:text-xl",
    heading4: "text-base sm:text-xl font-light",
    heading5: "text-base sm:text-xl font-extralight",

    flexCenter: "flex justify-center items-center",
    flexStart: "flex justify-start items-start",
    flexEnd: "flex justify-end items-end",

    paddingX: "sm:px-6 px-4",
    paddingY: "sm:py-6 py-4",
    padding: "sm:px-6 px-4 sm:py-6 py-4",

    paddingButton: "py-2 px-4",

    marginX: "sm:mx-6 mx-4",
    marginY: "sm:my-6 my-4",
    margin: "sm:mx-6 mx-4 sm:my-6 my-4",

    floatingActionButtonPositionRight: "fixed bottom-28 right-0",
    floatingActionButtonPositionLeft: "fixed bottom-28 left-0",

    spaceBetweenX: "space-x-4",
    spaceBetweenY: "space-y-4",

    header: "shadow-2xl rounded-b-2xl",
    card: "sm:space-x-96 sm:w-[52rem] space-x-4 w-[22rem] justify-between shadow-2xl rounded-2xl"
};

export const layout = {
    section: `flex md:flex-row flex-col ${styles.paddingY}`,
    sectionReverse: `flex md:flex-row flex-col-reverse ${styles.paddingY}`,

    sectionImgReverse: `flex-1 flex ${styles.flexCenter} md:mr-10 mr-0 md:mt-0 mt-10 relative`,
    sectionImg: `flex-1 flex ${styles.flexCenter} md:ml-10 ml-0 md:mt-0 mt-10 relative`,

    sectionInfo: `flex-1 ${styles.flexStart} flex-col`,
};